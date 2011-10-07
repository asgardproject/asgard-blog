from django.conf.urls.defaults import patterns, url

from blog import feeds
from blog import views

urlpatterns = patterns('',
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
		view = views.BlogPostDeatilView.as_view(),
		name = 'blog_post_detail',
	),
	# 
	# Archive
	#
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 
		view = views.BlogPostDayArchiveView.as_view(),
		name = 'blog_archive_day',
	),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
		view = views.BlogPostMonthArchiveView.as_view(),
		name = 'blog_archive_month',
	),
	url(r'^(?P<year>\d{4})/(?P<week>\w{1,2})/(?P<weekday>[a-z]{3})/$',
		view = views.BlogPostWeekDayArchiveView.as_view(),
		name = 'blog_archvie_weekday',
	),
	url(r'^(?P<year>\d{4})/(?P<week>\w{1,2})/$',
		view = views.BlogPostWeekArchiveView.as_view(),
		name = 'blog_archvie_week',
	),
	url(r'^(?P<year>\d{4})/$',
		view = views.BlogPostYearArchiveView.as_view(),
		name = 'blog_archive_year',
	),
	url(r'^updated/feed/$',
		view = feeds.BlogUpdatedPostFeed(),
		name = 'blog_updated_post_feed',
	),
	url(r'^updated/$',
		view = views.BlogPostUpdatedArchiveView.as_view(),
		name = 'blog_updated',
	),
	url(r'^archive/$',
		view = views.BlogPostArchiveView.as_view(),
		name = 'blog_archive',
	),
	url(r'^feed/$',
		view = feeds.BlogPostFeed(),
		name = 'blog_post_feed',
	),
	
	#
	# Search
	#
	url(r'^search/$',
		view = views.BlogPostSearchFormListView.as_view(),
		name = 'blog_archive',
	),
	
	#
	# Tag
	#
	url(r'^tag/(?P<slug>(.*))/feed/$',
		view = feeds.BlogTagPostFeed(),
		name = 'blog_tag_post_feed',
	),
	
	#
	# Category
	# 
	url(r'^category/(?P<slug>[-\w]+)/feed/$',
		view = feeds.BlogCategoryPostFeed(),
		name = 'blog_category_post_feed'
	),
	url(r'^category/(?P<slug>[-\w]+)/page/(?P<page>\d+)/$',
		view = views.BlogCategoryDetailView.as_view(),
		name = 'blog_categories_detail_paginated',
	),
	url(r'^category/(?P<slug>[-\w]+)/$',
		view = views.BlogCategoryDetailView.as_view(),
		name = 'blog_categories_detail',
	),
	url(r'^category/$',
		view = views.BlogCategoryListView.as_view(),
		name = 'blog_categories_list',
	),
	
	#
	# Author
	#
	url(r'^author/(?P<username>[-\w]+)/feed/$',
		view = feeds.BlogAuthorPostFeed(),
		name = 'blog_author_post_feed'
	),
	
	#
	# Index
	#
	url(r'^page/(?P<page>\d+)/$',
		view = views.BlogPostListView.as_view(),
		name = 'blog_index_paginated',
	),
	url(r'^$',
		view = views.BlogPostListView.as_view(),
		name = 'blog_index',
	),
)

urlpatterns += patterns('blog.views.old_views',
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$',
		view = 'detail',
		name = 'blog_post_detail',
	),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 
		view = 'archive_day',
		name = 'blog_archive_day',
	),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
		view = 'archive_month',
		name = 'blog_archive_month',
	),
	url(r'^(?P<year>\d{4})/$',
		view = 'archive_year',
		name = 'blog_archive_year',
	),
	url(r'^tag/(?P<slug>(.*))/page/(?P<page>\d+)/$',
		view = 'tag_detail',
		name = 'blog_tag_detail_paginated',
	),
	url(r'^tag/(?P<slug>(.*))/$',
		view = 'tag_detail',
		name = 'blog_tags_detail',
	),
	url(r'^tag/$',
		view = 'tag_list',
		name = 'blog_tags_list'
	),
	url(r'^category/(?P<slug>[-\w]+)/page/(?P<page>\d+)/$',
		view = 'category_detail',
		name = 'blog_categories_detail_paginated',
	),
	url(r'^category/(?P<slug>[-\w]+)/$',
		view = 'category_detail',
		name = 'blog_categories_detail',
	),
	url(r'^category/$',
		view = 'category_list',
		name = 'blog_categories_list',
	),
	url(r'^author/(?P<username>[-\w]+)/page/(?P<page>\d+)/$',
		view = 'author_detail',
		name = 'blog_authors_detail_paginated',
	),
	url(r'^author/(?P<username>[-\w]+)/$',
		view = 'author_detail',
		name = 'blog_authors_detail',
	),
	url(r'^author/$',
		view = 'author_list',
		name = 'blog_authors_list'
	),
	url(r'^updated/$',
		view = 'updated',
		name = 'blog_updated',
	),
	url(r'^search/$',
		view = 'search',
		name = 'blog_search',
	),
	url(r'^archive/$',
		view = 'archive',
		name = 'blog_archive'
	),
)
