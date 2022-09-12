import copy
"""
    Prototype pattern : 기존 객체를 복사하여 새로운 객체를 생성
    # copy.deepcopy
    # ex. 여러 웹 사이트를 이름, 도메인, 생성일자만 바꿔서 새롭게 생성
"""

class Website:

    def __init__(self, name, domain, description, author, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = [f"Website {self.name}\n"]
        infos = vars(self).items()

        ordered_info = sorted(infos)
        for attr, val in ordered_info:
            if attr == "name":
                continue
            summary.append(f"{attr}:{val}")
        return "".join(summary)

class Prototype:

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])
        return obj

def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website("ContentGardening",
                    domain = "contentgardening.com",
                    description="Automation and data-drivend apps",
                    author="Kamon Ayeva",
                    category = "Blog",
                    keywords=keywords)
    prototype = Prototype()
    identifier = 'ka-cg-1'
    prototype.register(identifier, site1)
    site2 = prototype.clone(identifier,
                            name="ContentGardeningPlayground",
                            domain="play.contentgardening.com",
                            description="Experimentation for tech featured on the blog",
                            category="Membership site",
                            create_date = "2018-08-01")
    for site in (site1, site2):
        print(site)
    print(f"site1 ID : {id(site1)} != site2 ID : {id(site2)}")

if __name__ == "__main__":

    main()

