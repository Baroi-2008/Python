def simulate_phishing_scenario():
    print("Welcome to the Cybersecurity Training Program!")
    print("This is a safe environment to learn about phishing attacks.")
    
    # Simulate receiving an email
    email_content = """
    Dear User,

    We noticed unusual activity on your account. Please click the link below to verify your identity:

    [ FAKE LINK: http://phishing-example.com ]

    Thank you,
    The Security Team
    """
    
    print("You received the following email:")
    print(email_content)

    # User input simulation
    response = input("Do you click the link? (yes/no): ").strip().lower()
    
    if response == "yes":
        print("This was a phishing attempt! In a real-world scenario, clicking the link could have compromised your account.")
    else:
        print("Good choice! Always be cautious with unsolicited links.")

# Run the simulation
simulate_phishing_scenario()