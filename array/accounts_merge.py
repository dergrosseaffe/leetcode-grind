class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, query):
        if query not in self.parent:
            self.parent[query] = query
        elif self.parent[query] != query:
            self.parent[query] = self.find(self.parent[query])

        return self.parent[query]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        emailToName = {}

        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            for email in account[1:]:
                uf.union(email, firstEmail)     # merges all emails with first email
                emailToName[email] = name

        rootEmails = defaultdict(list)
        for email in emailToName.keys():
            rootEmail = uf.find(email)
            rootEmails[rootEmail].append(email)

        result = []
        for rootEmail, emails in rootEmails.items():
            name = emailToName[rootEmail]
            result.append([name] + sorted(emails))

        return result
