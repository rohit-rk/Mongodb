#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades
query = {'type':'homework'}
try:
    docs = grades.find(query)
    docs.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
    
except Exception as e:
    print "Error occured" ,type(e),e

count = 1
for doc in docs:
    if (count % 2 == 0):
        continue
    doc.delete_one()
    count =count + 1
    
    print "done"
        
