data = [
{
  "from" : "&quot;Andy Bedard&quot; &lt;fcdenver@...&gt;, emerson.brandao@...",
  "authorName" : "Andy Bedard , emerson.brandao@terra.com.b"
},
{
  "from" : "Lance Dockery &lt;lance.dockery@...&gt;",
  "authorName" : "Lance Dockery"
}]

def dumbfun(data):

    # parse out the from to keep only the email. If th
    if '&lt;' in data['from'] or '&gt;'in data['from']:
        assert '&lt;' in data['from'] and '&gt;' in data['from']
        stripped_name, from_remainder = data['from'].split('&lt;', 1)
        stripped_name = stripped_name.strip()
        # make sure we're not losing any information
        if stripped_name.startswith("&quot;"):
            assert stripped_name.endswith("&quot;")
            stripped_name = stripped_name[6:-6].strip()

            # check that the stripped names match
            # but if we have a weird encoding thing then forget it
            if not stripped_name.startswith("=?"):
                if stripped_name.startswith("&quot;"):
                    assert stripped_name.endswith("&quot;")
                    stripped_name = stripped_name[6:-6].strip()

                check_authorname = data['authorName'].strip()
                # if we have an email, ignore the domain
                if '@' in stripped_name:
                    assert '@' in data['authorName']
                    stripped_name = stripped_name.split('@', 1)[0].strip()
                    check_authorname = check_authorname.split('@', 1)[0].strip()

                print(stripped_name)
                print(check_authorname.strip())
                assert stripped_name == check_authorname.strip(), "Stripped name %s didn't match " \
                    "author name %s (check name was %s)" % (
                        stripped_name, data['authorName'], check_authorname,
                    )

            # leave only the email in
            data['from'], leftover = from_remainder.split('&gt;', 1)
            # make sure lost nothing on the right side
            assert not leftover.strip()


if __name__ == '__main__':
    dumbfun(data[1])
