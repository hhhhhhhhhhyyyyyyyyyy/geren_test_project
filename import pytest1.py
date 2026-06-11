import pytest
import requests
from selenium import webdriver
import pymysql
import allure

print("✅ pytest 版本:", pytest.__version__)
print("✅ requests 版本:", requests.__version__)
print("✅ selenium 版本:", webdriver.__version__)
print("✅ pymysql 版本:", pymysql.__version__)
print("✅ allure 版本:", allure.__version__)
print("\n🎉 所有核心库导入成功！")