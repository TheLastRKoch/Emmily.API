from rest_framework.test import APITestCase
from wordlist_skill.models import Word

class WordCreateTestCase(APITestCase):
    def test_create_word(self):
        dummy_word = {
            'word':"Parallelepiped",
            'language':"EN-US"
        }
        response = self.client.post('/api/v1/wordlist/new',dummy_word)
        if response.status_code != 201:
            print(response.content)

class WordDestroyTestCase(APITestCase):
    def test_delete_word(self):
        initial_word_count = Word.objects.count()
        custom_word = Word.objects.first()
        word_id = Word.objects.first().id
        self.client.dete('/api/v1/wordlist/{}'.format(word_id))
        self.assertEqual(
            Word.objects.count(),
            initial_word_count-1
        )
        self.assertRaises(
            Word.DoesNotExist,
            Word.objects.get, id=word_id
        )