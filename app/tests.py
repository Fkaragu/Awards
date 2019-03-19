from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile

class Image_TestCases(TestCase):
    def setUp(self):

        self.new_project = Project(id=1,photo='media/articles/Nature.jpg',proj_title='Nature', proj_link='https://thashpitch.herokuapp.com',proj_description='Test',post_date='15-03-2019')
        self.new_profile = Profile(id=1,profile_pic='media/articles/Nature.jpg',bio='The one and only admin', projects_id='1',contact='07190000',user_id=1)
        self.new_project.save_project()
        self.new_profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()

    def test_is_instance(self):

        self.assertTrue(isinstance(self.new_project,Project))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_project.save_project()
        all_obj = Project.objects.all()
        self.assertTrue(len(all_obj)>0)

    def test_delete_method(self):
        self.new_project.save_project()
        obj_filt = Project.objects.filter(proj_title='Nature')
        Project.delete_project(obj_filt)
        obj_all = Project.objects.all()
        self.assertTrue(len(obj_all) == 0)
