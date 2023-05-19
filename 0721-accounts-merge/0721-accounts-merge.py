class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        emails = {}
        parent = [i for i in range(len(accounts))]
        size =   [1 for i in range(len(accounts))]
        answer = defaultdict(list)
        final_answer = []
        def find(account):
            
            if parent[account] == account:
                return account
            
            parent[account] = find(parent[account])
            return parent[account]
        
        def union(account1,account2):
            par1 = find(account1)
            par2 = find(account2)
            
            if par1 == par2:
                return
            
            if size[par2] > size[par1]:
                par1,par2 = par2,par1
                
            size[par1] += size[par2]
            parent[par2] = par1
        
        for account in range(len(accounts)):
            
            for emailIdx in range(1,len(accounts[account])):
                
                if accounts[account][emailIdx] not in emails:
                    emails[accounts[account][emailIdx]] = account
                
                union(account,emails[accounts[account][emailIdx]])
        
        for email in sorted(emails):
            answer[find(emails[email])].append(email)
        
        for key in answer.keys():
            final_answer.append([accounts[key][0]] + (answer[key]))
        
        return final_answer
        
            
            
            
        