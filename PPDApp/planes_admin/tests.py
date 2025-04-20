import sys

from django.test import TestCase
from django.conf import settings
import sys

def test_verificar_settings():
    print("\n⚙️ Django está usando:", settings.SETTINGS_MODULE)
    print(settings.TESTING)
    esta=any("pytest" in palabra for palabra in sys.argv)
    print(esta)
# Create your tests here.
