from django.test import TestCase

# Create your tests here.
print 123

class myTestCase(TestCase):
    def setUp(self):
        self.lion = 123
        
    def testSpeaking(self):
        self.assertEqual('the lion says "roar"', 'The lion says "roar"')

    def testSpeaking2(self):
	self.assertEqual('The lion says "roar"', 'The lion says "roar"')
