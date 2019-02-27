# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        #item = str(item)
        #filesName = 'dangdangshu.txt'
        with open("dangdangshu.txt", "a") as f:
            for i in range(0,len(str(item['name']))):
                f.write(str(item['name'][i] + '\t'))
                f.write(str(item['title'][i] + '\t'))
                f.write(str(item['time'][i] + '\t'))
                f.write(str(item['price'][i] + '\t'))
                f.write('\n')


            f.close()
        return item


