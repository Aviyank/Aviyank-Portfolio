#!/usr/bin/env python
"""
Quick script to generate a Django SECRET_KEY for deployment.
Run this before deploying to get a secure secret key.
"""
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("Your Django SECRET_KEY:")
    print("="*60)
    print(secret_key)
    print("="*60)
    print("\nCopy this and use it as your SECRET_KEY environment variable")
    print("in Railway or Render dashboard.\n")

