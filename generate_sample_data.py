"""Script to generate sample data."""
# ruff: noqa

import argparse
import os

import django

# Parse CLI args.
parser = argparse.ArgumentParser()
parser.add_argument("--num-blogs", type=int, default=10)
parser.add_argument("--num-posts", type=int, default=100)
args = parser.parse_args()

# Load settings.
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

# # Flush current data.
# call_command("flush", "--noinput")
# print("Flushed existing db.")
#
# # Create a superuser.
# os.environ["DJANGO_SUPERUSER_PASSWORD"] = "pw"
#
# cmd = "createsuperuser --username admin"
# cmd += " --email admin@admin.com"
# cmd += " --noinput"
#
# cmd_parts = cmd.split()
# call_command(*cmd_parts)

# Create sample blogs.
from model_factories import BlogFactory, BlogPostFactory

for _ in range(args.num_blogs):
    BlogFactory.create()
print(f"Generated {args.num_blogs} sample blogs.")

for _ in range(args.num_posts):
    BlogPostFactory.create()
print(f"Generated {args.num_posts} sample posts.")
