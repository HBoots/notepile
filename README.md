# NOTE PILE

(Dev_Notes app in Django)

A set of personal notes on various software and web development technologies.

The site is intended to provide quick reference from any location without the need to log into Github or any other account.

## Admin Access

During development:

-   Superuser: dreche / drechepassword
-   DevelopementUser: dev / devpassword

Change Admin username and password before deployment.

Create a separate user developer account.

## Do

-   change table styling
-   change fenced code styling (js library that adds syntax highlighting)
-   create offcanas list items with db topic data
-   database filter with new view for each topic ?
-   enter the rest of dev_notes markdown
-   read up on how converted markdown is sanitized.
    -   add separate santizer ?
-   Notes lists: change to grid instead of stacked? Have buttons that switch from one to the other?

## Notes

-   Odd behavior results when using the `slice` filter in the templates when the text being sliced is in a table. Sometimes the table will be give formatting from a previous entry. Sometimes the following entry will be entered into the table.
    -   Reason:
        -   The slice slices off the closing tag for the markdown so the browser adds it in odd places.
        -   So bold, italics, tables that have closing tags in MARKDOWN will have everything following put inside when the browser adds the closing tags.
    -   Solutions:
        -   Instead of slicing the text, add a field that will be displayed on the list page and limit the text length in the model.
        -   Filter markdown out ??
