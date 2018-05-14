class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    if records:
        if records[-1].record_id != len(records) - 1:
            raise ValueError("Error")
        if records[0].record_id != 0:
            raise ValueError("Error")
    trees = []
    for j in records:
        if (j.record_id > j.parent_id) and (j.parent_id >= 0):
            trees.append(Node(j.record_id))
            trees[j.parent_id].children += [trees[-1]]
        elif (j.record_id == 0) and (j.parent_id == 0):
            trees.append(Node(j.record_id))
        else:
            raise ValueError("Error")
    if len(trees) > 0:
        root = trees[0]
    return root
