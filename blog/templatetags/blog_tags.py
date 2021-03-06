import re
from math import log

from django import template
from django.conf import settings
from django.db import models

Post = models.get_model('blog', 'post')
Category = models.get_model('blog', 'category')

register = template.Library()

class LatestPosts(template.Node):
	"""
	TODO
	"""
	def __init__(self, limit, var_name):
		self.limit = limit
		self.var_name = var_name
	
	def render(self, context):
		posts = Post.objects.published()[:int(self.limit)]
		if (int(self.limit) == 1):
			context[self.var_name] = posts[0]
		else:
			context[self.var_name] = posts
		
		return ''

@register.tag
def get_latest_posts(parser, token):
	"""
	Gets any number of latest posts and stores them in a varable.
	
	Syntax::
		
		{% get_latest_posts [limit] as [var_name] %}
	
	Example usage::
		
		{% get_latest_posts 10 as latest_post_list %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	
	m = re.search(r'(.*?) as (\w+)', arg)
	
	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
	
	format_string, var_name = m.groups()
	
	return LatestPosts(format_string[0], var_name)

class BlogCategories(template.Node):
	"""
	TODO
	"""
	def __init__(self, var_name):
		self.var_name = var_name
	
	def render(self, context):
		categories = Category.objects.all()
		context[self.var_name] = categories
		return ''

@register.tag
def get_blog_categories(parser, token):
	"""
	Gets all blog categories.

	Syntax::

		{% get_blog_categories as [var_name] %}

	Example usage::

		{% get_blog_categories as category_list %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	m = re.search(r'as (\w+)', arg)
	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
	var_name = m.groups()[0]
	return BlogCategories(var_name)

@register.filter
def get_links(value):
	"""
	Extracts links from a ``Post`` body and returns a list.

	Template Syntax::

		{{ post.body|markdown|get_links }}

	"""
	try:
		try:
			from BeautifulSoup import BeautifulSoup
		except ImportError:
			from beautifulsoup import BeautifulSoup
		soup = BeautifulSoup(value)
		return soup.findAll('a')
	except ImportError:
		if settings.DEBUG:
			raise template.TemplateSyntaxError, "Error in 'get_links' filter: BeautifulSoup isn't installed."
	return value

def strip_illustrations(parser):
	"""
	Strip illustrations from the given blog entry copy.  This is used
	in feed templates, as without CSS applied illustrations look ass.
	
	As an example, given the string::
	
	>>> s = '<p class="illustration"><img /> A caption.</p>'
	>>> strip_illustrations(s)
	''
	>>> s = '<p>Keep this.</p><p class="illustration"><img /></p><p>And this.</p>'
	>>> strip_illustrations(s)
	'<p>Keep this.</p><p>And this.</p>'
	"""
	from BeautifulSoup import BeautifulSoup
	soup = BeautifulSoup(parser)
	illustrations = soup.findAll("p", {"class": "illustration"})
	[illustration.extract() for illustration in illustrations]
	return str(soup)

register.filter('strip_illustrations', strip_illustrations)
