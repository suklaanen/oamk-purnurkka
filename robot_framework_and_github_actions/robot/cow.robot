*** Settings ***
Documentation    Cow Says Meow
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***
${BASE_URL}    http://localhost:80

*** Test Cases ***
Test Cowsay Says Meow
    [Documentation]    Cowsay Says Meow
    Open Browser    about:blank    browser=firefox
    Cow says    Meow
    ${response}=    Get response
    Log    Response: ${response}
    Should Contain    ${response}    Meow
    Sleep    2s
    Close Browser

*** Keywords ***
Cow says
    [Arguments]    ${sayThis}
    Go to Base URL    ${sayThis}

Get response 
    ${response}=    Execute Javascript    return document.body.textContent
    [Return]    ${response}

Go to Base URL
    [Arguments]    ${sayThis}
    Go To    ${BASE_URL}/${sayThis}