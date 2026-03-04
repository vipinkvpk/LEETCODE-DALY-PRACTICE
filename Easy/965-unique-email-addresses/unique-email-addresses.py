class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local_name, domain_name= email.split("@")
            processed_local= []
            for char in local_name:
                if char == ".":
                    continue 
                if char == "+":
                    break 
                processed_local.append(char)
            normalized_email="".join(processed_local)+"@"+domain_name
            unique_emails.add(normalized_email)
        return len(unique_emails)

        