class Solution:
    # time - O(E logE), space - O(E) - E = total unique emails
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        parent = {}
        rank = {}

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

            return True

        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            if firstEmail not in parent:
                parent[firstEmail] = firstEmail
                rank[firstEmail] = 0
                emailToName[firstEmail] = name
            for i in range(2, len(account)):
                currentEmail = account[i]
                if currentEmail not in parent:
                    parent[currentEmail] = currentEmail
                    rank[currentEmail] = 0
                    emailToName[currentEmail] = name
                union(firstEmail, currentEmail)

        group = defaultdict(list)

        for email in parent.keys():
            root = find(email)
            group[root].append(email)

        res = []
        for root in group.keys():
            name = emailToName[root]
            emails = sorted(group[root])
            res.append([name] + emails)

        return res
