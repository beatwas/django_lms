def qs2html(qs_list):
    s = '<table>'
    for record in qs_list:
        s += f'<tr><td>{record.first_name}</td><td>{record.last_name}</td>' \
             f'<td>{record.email}</td>td>{record.phone}</td></tr> '
    s += '</table>'

    return s
