# QApp/Backend/data_access.py
DOCS = {
    "docker": "Docker packages applications and their dependencies.",
    "image": "An image is a blueprint used to create containers.",
    "container": "A container is a running instance of an image.",
    "port": "Port mapping connects your machine to a port inside the container."
}
 
def get_docs():
    return DOCS
