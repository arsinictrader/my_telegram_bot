#!/usr/bin/env bash

echo "📦 جاري تثبيت المكتبات المطلوبة..."
pip install --upgrade pip
pip install --no-cache-dir --force-reinstall -r requirements.txt
