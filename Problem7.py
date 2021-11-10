import collections

class RouteNode(object):
    def __init__(self, handler = ''):
        self.children = {}
        self.handler = handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, defHandler):
        self.root = RouteNode()
        self.defHandler = defHandler
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, name = None):
        self.path = split_path(path)
        self.name = name
        current_node = self.root
        for _ in self.path:
            if _ not in current_node.children:
                current_node.children[_] = RouteNode(name)
            current_node = current_node.children[_]
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, path):
        self.path = split_path(path)
        current_node = self.root
        if path == '/':
            return self.defHandler
        for _ in self.path:
            if _ not in current_node.children:
                return None
            current_node = current_node.children[_]
        return current_node.handler
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


def split_path(path):
    splitPathList = []
    splitPath = ''
    for _ in range(len(path)):
        if path[_] == '/' and _ != 0:
            splitPathList.append(splitPath)
            splitPath = path[_]
        elif _ == len(path) - 1:
            splitPath += path[_]
            splitPathList.append(splitPath)
        else:
            splitPath += path[_]
    return splitPathList
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
