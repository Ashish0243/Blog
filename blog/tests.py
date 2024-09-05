from django.test import TestCase,Client
from .models import PostsCollection
from django.contrib.auth import get_user_model
from django.urls import reverse
class TestUnderWay(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='test123'
        )
        self.post=PostsCollection.objects.create(
            title="A good Title",
            body='A good Body',
            author=self.user
            
        )
        
    def test_str_rep(self):
        self.assertEqual(str(self.post),'A good Title')
        
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good Title')
        self.assertEqual(f'{self.post.body}','A good Body')
        self.assertEqual(f'{self.post.author}','testuser')
        
    def test_post_list_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'A good Body')
        self.assertTemplateUsed(response,'home.html')
        
    def test_post_detail_view(self):
        response=self.client.get('/post/1/',follow=True)
        self.assertEqual(response.status_code,200)
        noresponse=self.client.get('/post/20/')
        self.assertEqual(noresponse.status_code,404)
        self.assertContains(response, 'A good Title')
        self.assertTemplateUsed(response, 'detail.html')
        
    def test_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')
        
    def test_create_view(self):
        response=self.client.post(reverse('new_post'),
                                  {
                                      'title':'good title',
                                      'body':'good body',
                                      'author':self.user
                                  })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'good title')
        self.assertContains(response,'good body')
    
    def test_edit_view(self):
        response=self.client.post(reverse('edit_post',args='1'),{
            'title':"updated title",
            'body':"updated body"
        })
        self.assertEqual(response.status_code,302)
        
    def test_delete_view(self):
        response=self.client.get(reverse('delete_post',args='1'))
        self.assertEqual(response.status_code,200)
        


