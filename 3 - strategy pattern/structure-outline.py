# structure-outline
# Note: this file does not run
# Create an interface for the strategy (1)

import string
import random
from typing import List
from abc import ABC
from abc import abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Note: order of class SupportTicket must be before the stategy class
# or the class is undefined.
class SupportTicket:

    def __init__(self, customer, issue):
            self.id = generate_id()
            self.customer = customer
            self.issue = issue

# Add the TicketOrderingStrategy class (2)
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

# Add each strategy with their own create_ordering method (3)
# This allows the user to define the type at instance of object.
class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        # add method
        return list


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        # add method
        return list

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        # add method
        return list

class CustomerSupport:

    # Define tickets, not in example but in video. (A1)
    tickets: List[SupportTicket] = []

    # Delete Init (A2)

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    # Get the Strategy (4)
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        
        # create the ordered list (5)
        ticket_list = processing_strategy.create_ordering(self.tickets)

        # Move the test condition because the strategy may delete objects (6)
        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
# remove the string definition of strategies (7)
# replace string with the type of ordering strategy
app = CustomerSupport(RandomOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
