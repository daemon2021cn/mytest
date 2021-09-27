from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        email_name = []

        for email_cur in emails:
            email_split = email_cur.split('@')
            email_l = email_split[0]
            email_d = email_split[1]

            name_l = ""
            for name in email_l.split('.'):
                name_l += name
            name_l = name_l.split('+')[0]

            if name_l+'@'+email_d not in email_name:
                count += 1
                email_name.append(name_l+'@'+email_d)

        return count

classNew = Solution()
emails = list(input().split())
results = classNew.numUniqueEmails(emails)
print(results)
