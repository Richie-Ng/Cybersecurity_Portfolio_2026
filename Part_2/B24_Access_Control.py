print("[*] Initializing Role-Based Access Control (RBAC) Engine...")

# 1. Define the Access Control Matrix (Roles and Permissions)
role_permissions = {
    "Administrator": ["view_public", "access_dashboard", "edit_users", "view_classified_intel"],
    "Analyst": ["view_public", "access_dashboard"],
    "Guest": ["view_public"]
}

# 2. Define the User Database (Identity and Assigned Roles)
user_database = {
    "alice_admin": "Administrator",
    "bob_analyst": "Analyst",
    "charlie_guest": "Guest"
}

# 3. The Access Control Logic (The Gatekeeper)
def request_access(username, resource):
    print(f"--> [AUTH REQUEST] User '{username}' attempting to access '{resource}'...")
    
    # Check if user exists (Authentication)
    if username not in user_database:
        print("    [DENIED] Authentication failed: Unknown user.\n")
        return

    # Check user permissions (Authorization)
    user_role = user_database[username]
    allowed_resources = role_permissions.get(user_role, [])

    if resource in allowed_resources:
        print(f"    [GRANTED] Authorization approved. Role '{user_role}' has access.\n")
    else:
        print(f"    [DENIED] Authorization blocked. Role '{user_role}' lacks privileges. Incident Logged.\n")

# 4. Simulate Real-World Access Requests
print("\n=== EXECUTING ACCESS CONTROL SIMULATIONS ===")

# Test 1: Admin accessing high-level intel (Should Grant)
request_access("alice_admin", "view_classified_intel")

# Test 2: Analyst trying to access high-level intel (Should Deny - Privilege Escalation Attempt)
request_access("bob_analyst", "view_classified_intel")

# Test 3: Analyst accessing their normal dashboard (Should Grant)
request_access("bob_analyst", "access_dashboard")

# Test 4: Guest trying to access the dashboard (Should Deny)
request_access("charlie_guest", "access_dashboard")

# Test 5: Unknown user trying to access public data (Should Deny)
request_access("eve_hacker", "view_public")

print("[*] RBAC Simulation Complete.")
