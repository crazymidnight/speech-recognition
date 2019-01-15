"""Client app."""

import os
from flask import Blueprint

client_bp = Blueprint("client_app", __name__,
                      url_prefix="",
                      static_url_path="",
                      static_folder="../frontend/dist/",
                      template_folder="../frontend/dist/")
