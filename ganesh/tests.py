from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Certification


class CertificationOrderTest(TestCase):
    def setUp(self):
        self.client = Client()
        # sort_order: A=1, B=2, C=3 → expected homepage order: A, B, C
        Certification.objects.create(title='Cert A', image='certification/a.png', link='https://a.com', sort_order=1)
        Certification.objects.create(title='Cert B', image='certification/b.png', link='https://b.com', sort_order=2)
        Certification.objects.create(title='Cert C', image='certification/c.png', link='https://c.com', sort_order=3)

    def test_certifications_ordered_by_sort_order(self):
        """Certifications queryset must follow sort_order, not insertion order."""
        certs = list(Certification.objects.order_by('sort_order').values_list('title', flat=True))
        self.assertEqual(certs, ['Cert A', 'Cert B', 'Cert C'])

    def test_homepage_reflects_sort_order(self):
        """Homepage must render certifications in sort_order sequence."""
        from .models import Home, About, Resume
        Home.objects.create(name='G', greetings_1='Hi', greetings_2='Hey', picture='picture/p.png')
        About.objects.create(heading='H', career='Dev', description='Desc', profile_img='profile/p.png')
        Resume.objects.create(link='https://resume.com')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        pos_a = content.index('Cert A')
        pos_b = content.index('Cert B')
        pos_c = content.index('Cert C')
        self.assertLess(pos_a, pos_b)
        self.assertLess(pos_b, pos_c)

    def test_sort_order_update_reflects_on_homepage(self):
        """Changing sort_order of a cert must change its position on homepage."""
        from .models import Home, About, Resume
        Home.objects.create(name='G', greetings_1='Hi', greetings_2='Hey', picture='picture/p.png')
        About.objects.create(heading='H', career='Dev', description='Desc', profile_img='profile/p.png')
        Resume.objects.create(link='https://resume.com')

        # Move Cert C to first position
        Certification.objects.filter(title='Cert C').update(sort_order=0)
        response = self.client.get('/')
        content = response.content.decode()
        pos_c = content.index('Cert C')
        pos_b = content.index('Cert B')
        self.assertLess(pos_c, pos_b)
