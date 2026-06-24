class Solution:
    # time - O(E logE) space - O(E) - E = unique emails
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        emailToAccount = {}
        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            emailToAccount[firstEmail] = name
            graph[firstEmail]
            for index in range(2,len(account)):
                currentEmail = account[index]
                emailToAccount[currentEmail] = name
                graph[firstEmail].append(currentEmail)
                graph[currentEmail].append(firstEmail)

        visit = set()
        res = []

        def dfs(email, connected):
            if email in visit:
                return connected
            visit.add(email)
            connected.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, connected)
            return connected

        for email in graph.keys():
            if email not in visit:
                group = dfs(email, [])
                ans = []
                ans.append(emailToAccount[email])
                ans += sorted(group) if group else group
                res.append(ans)
        
        return res
