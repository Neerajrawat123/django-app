import os
from django.core.management.base import BaseCommand
from myApp.models import  MarketInsight
from datetime import datetime
import json

class Command(BaseCommand):
    help = 'Import JSON data into database'

    
    def handle(self, *args, **kwargs):
        # Construct the absolute file path
        json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'jsondata.json'))
        
        # Check if the file exists
        if os.path.exists(json_file_path):
            # Open the JSON file and load the data
            with open(json_file_path,encoding='utf-8') as f:
                data = json.load(f)
                # Iterate over the JSON data and create model instances
                for item in data:
                    if item['end_year'] == '':
                        item['end_year'] = 0
                        
                    if item['start_year'] == '':
                        item['start_year'] = 0
                     
                    if item['intensity'] == '':
                        item['intensity'] = 0
                        
                    if item['likelihood'] == '':
                        item['likelihood'] = 0
                        
                    if item['relevance'] == '':
                        item['relevance'] = 0
                     
                    item['published'] = changeDate(item['published'])
                    item['added'] = changeDate(item['added'])


                    MarketInsight.objects.create(
                         insight = item['insight'],
                         url = item['url'],
                         region = item['region'],
                         published = item['published'],
                         added = item['added'],
                         relevance  = item['relevance'],
                         pestle = item['pestle'],
                         title  = item['title'],
                         likelihood = item['likelihood'],
                         intensity = item['intensity'],
                         topic = item['topic'],
                         end_year = item['end_year'],
                         sector = item['sector'],
                         start_year = item['start_year'],
                         impact = item['impact'],
                         country = item['country'],
                         source = item['source'],

                         )
            # Display success message
            self.stdout.write(self.style.SUCCESS('Successfully imported JSON data'))
        else:
            # Display error message if file not found
            self.stdout.write(self.style.ERROR('JSON file not found at: {}'.format(json_file_path)))
            
            
def changeDate(date):
    if date == '':
        date = None
        return date
    try:
        date_obj1 = datetime.strptime(date, '%B, %d %Y %H:%M:%S')
        return date_obj1.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Invalid date format")
              
    