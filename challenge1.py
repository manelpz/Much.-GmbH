
elements = [{
    "id": 1,
    "name": "oil",
    "parent_id": None,
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



def food(element):
    str = ""
    index = 0
    

    if [element[index]["parent_id"]]:
        #NOT WORKING 
        # str += food(elements[index][element[index]["parent_id"]])
        #str += getName(elements[element.parentId[0] - 1]) + ", "
   
        str += element[index]["name"]
        return str

for e in elements[0]:
    print(food(elements))



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