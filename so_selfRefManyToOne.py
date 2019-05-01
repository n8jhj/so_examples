# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('node.id'))
    data = Column(String(50))
    parent = relationship("Node", remote_side=[id])

    def __repr__(self):
        return "Node(data={!r})".format(self.data)

# Setup.
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create tree.
node_tree = Node(data='root')
child1 = Node(data='child1', parent=node_tree)
child2 = Node(data='child2', parent=node_tree)
subchild1 = Node(data='subchild1', parent=child2)
subchild2 = Node(data='subchild2', parent=child2)
child3 = Node(data='child3', parent=node_tree)

# When child2 is added...
session.add(child2)
print(child3 in session)  # Result: False
