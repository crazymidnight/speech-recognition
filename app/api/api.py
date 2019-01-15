"""Client app."""

import os
from flask import Blueprint

api_bp = Blueprint("api_app", __name__,
                      url_prefix="",
                      static_url_path="",
                      static_folder="../dist/",
                      template_folder="../dist/")
