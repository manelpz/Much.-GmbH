
elements = [{
    "id": 1,
    "name": "oil",
    "parent_id": 1,
    "children_ids": [2,3]
},
{

    "id": 2,
    "name": "sunflower oil",
    "parent_id": 1,
    "children_ids": []
},
{
    "id": 3,
    "name": "olive oil",
    "parent_id": 1,
    "children_ids": [4]
},
{
    "id": 4,
    "name": "extra virgin olive oil",
    "parent_id":  3,
    "children_ids": []
}]


#[d['value'] for d in l]
#map(lambda d: d['value'], l)
#In[5]: ll = [{'value': 'apple', 'blah': 2}, {'value': 'banana', 'blah': 3} , {'value': 'cars', 'blah':4}]
#In[6]: ld = [d.get('value', None) for d in ll]

#d.get('value', None)

def food(element):
    str = ""
    index = 0
    
    #for key in element[index]:
    #print(element[0]["parent_id"]) 
        #print("key "+key)

    if [element[index]["parent_id"]]:
        #str = food(elements[index][element[index-1]["parent_id"]])
        
        print(element[index]["parent_id"])
    #return element[index]["name"]


    
 

    #if [element.get('parent_id', None) != None]:


        #return [i.get('name', None) for i in elements]
        
        #return [i.get('parent_id', None) for i in element]

        #str = food(elements[(element[0])])

    #return str #+=element[1]

for e in elements[0]:
    print(food(elements))

  
    #for key in element[index]:
    #print(element[0]["parent_id"]) 



'''
task revolved

const elements = [
  {
    "id": 1,
    "name": "oil",
    "parentId": [],
    "childrenIds": [2,3],
  },
  {
    "id": 2,
    "name": "olive oil",
    "parentId": [1],
    "childrenIds": [],
  },
  {
    "id": 3,
    "name": "sunflower oil",
    "parentId": [1],
    "childrenIds": [4],
  },
  {
    "id": 4,
    "name": "extra virgin olive oil",
    "parentId": [3],
    "childrenIds": [],
  },
];

function getName(element) {
  let str = "";
  if (element.parentId[0]) {
    str += getName(elements[element.parentId[0] - 1]) + ", "
  } 
  return str += element.name;
}

elements.forEach(e => console.log(getName(e)));

'''