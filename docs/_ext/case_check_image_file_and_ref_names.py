# This Sphinx extension checks for case mismatches between image
# references in .rst files and the actual image filenames in a specified
# directory. It's useful for avoiding broken links on case-sensitive
# file systems (like Linux).

# Import Sphinx's logging utility and the standard os module for file
# path operations
from sphinx.util import logging
import os

# Define the relative path to the image directory, and normalize it to
# ensure consistent formatting across operating systems (e.g.,
# converting backslashes to slashes, or the otherway around in Windows).
image_dir_path = os.path.normpath('assets/images')

# Create a logger instance for this module
logger = logging.getLogger(__name__)

# This function is called by Sphinx when the extension is set up
def setup(app):
    # Connect the 'builder-inited' event to the func: check_image_case
    # This means check_image_case runs after Sphinx builder initializes
    app.connect('builder-inited', check_image_case)

# This function checks for case mismatches between image references in
# .rst files and actual filenames
def check_image_case(app, exception=None):
    # Build the absolute path to the image directory by joining the
    # Sphinx source directory with the relative path
    image_dir = os.path.join(app.srcdir, image_dir_path)

    # If the image directory doesn't exist, log a warning and exit
    if not os.path.exists(image_dir):
        logger.warning(
            f"Extension: Case check image file and ref names: "
            f"Image dir not found {image_dir}"
        )
        return

    # Create a dictionary mapping lowercase filenames to their actual
    # case-sensitive names. This helps detect case mismatches later
    actual_files = {f.lower(): f for _, _, files in os.walk(image_dir) for f in files}

    # Iterate through all documents found by Sphinx
    for docname in app.builder.env.found_docs:
        # Construct the full path to the .rst file
        docpath = os.path.join(app.srcdir, docname + '.rst')

        # Open and read the file line by line
        with open(docpath, encoding='utf-8') as f:
            for lineno, line in enumerate(f, start=1):
                # Look for image or figure directives in the line
                if '.. image::' in line or '.. figure::' in line:
                    # Extract the image path from the directive
                    image_name = line.split('::')[1].strip()
                    # Get just the filename (without directory path)
                    image_basename = os.path.basename(image_name)

                    # Check if the lowercase version of the filename
                    # exists in the actual files
                    if image_basename.lower() in actual_files:
                        # Get the correct case-sensitive filename
                        correct_case = actual_files[image_basename.lower()]

                        # If the reference doesn't match the actual
                        # filename case, log an error
                        if image_basename != correct_case:
                            logger.error(
                                f"Case mismatch: image ref and filename, at {docpath}:{lineno}\n"
                                f"    reference: {image_basename}\n"
                                f"    filename:  {correct_case}"
                            )
