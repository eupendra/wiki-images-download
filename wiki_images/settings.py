
BOT_NAME = 'wiki_images'

SPIDER_MODULES = ['wiki_images.spiders']
NEWSPIDER_MODULE = 'wiki_images.spiders'
ITEM_PIPELINES={'scrapy.pipelines.images.ImagesPipeline':1}
IMAGES_STORE = 'local_folder'

ROBOTSTXT_OBEY = True
