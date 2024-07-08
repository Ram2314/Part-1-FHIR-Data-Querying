"""
For this assignment, you will choose any resource from the fhir server and display data similar to the
jupyter lesson. You cannot use any of the resources used in this parts lesson. Use https://www.hl7.org/fhir/us/core/
under `US Core Actors` to pick some data to use in this assignment. You will need to implement the following functions

1. display_data
2. author

display_data should display the data in the pattern consistent as follows:

|element_1|...element_n|...
|element_2|...|element_n|...

author should return a string with your name.
"""
import requests


def display_data(base_url: str, resource: str, patient_id: str) -> None:
    """
    Student implementation of display_data. This function should return data of 'your' choosing in the patter as
    described as above.

    Args:
        base_url (str): Base URL endpoint for the fhir server.
        resource (str): Resource name of your choosing to fetch the data from.
        patient_id (str): ID of patient you want to fetch the data from

    Return:
        None
    """
    # Student Code Goes Here

    raise NotImplemented


def author() -> str:
    """
    This function returns their name
    """
    return ''


if __name__ == '__name__':
    base_url = ''
    resource = ''
    patient_id = ''
    display_data(base_url=base_url, resource=resource, patient_id=patient_id)
