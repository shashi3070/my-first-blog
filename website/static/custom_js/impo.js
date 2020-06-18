function getinfo(d) {
    mapping = {}
    final_map = {}
    var parentid = []
    var typeofCompo = {}

    for (i = 0; i < d["blocks"].length; i++) {
        obj = d["blocks"][i];
        l = []
        ob = ''

        if (mapping[obj['parent']]) {
            l = mapping[obj['parent']]
            l = l.concat(obj['id'])
            mapping[obj['parent']] = l
        } else {
            l = l.concat(obj['id'])
            mapping[obj['parent']] = l
        }
        parentid.push(obj['parent'])
        //console.log(mapping)
        if (final_map[obj['parent']]) {
            ;
        } else {
            final_map[obj['parent']] = []
        }

        var list = []

        type = ''
        type = obj["data"][0]['value']
        //console.log(type)
        ob = {
            "level": obj['parent'],
            "type": obj["data"][0]['value']
        }
        //console.log(ob)
        if (type == "python") {
            console.log('python')
            //console.log(obj["data"][2]['name'])
            list.push(obj["data"][2]['value'])
            temp = final_map[obj['parent']]
            //console.log(temp)
            temp.push(list)
            //console.log(list)
            //console.log(temp)
            final_map[obj['parent']] = temp
            //console.log(final_map)
            typeofCompo[obj['parent']] = 'python'
            //console.log('python end')

        }
        if (type == "talend") {
            console.log('talend')
            //console.log(obj["data"][2]['name'])
            list.push(obj["data"][2]['value'])
            temp = final_map[obj['parent']]
            //console.log(temp)
            temp.push(list)
            //console.log(temp)
            final_map[obj['parent']] = temp
            //console.log(temp)
            typeofCompo[obj['parent']] = 'talend'
        }

        if (type == "matillion") {

            for (k = 2; k < 8; k++) {
                //console.log(obj["data"][k]['name'])
                list.push(obj["data"][k]['value'])
            }

            temp = final_map[obj['parent']]
            //console.log(final_map)
            temp.push(list)

            final_map[obj['parent']] = temp
            typeofCompo[obj['parent']] = 'matillion'

        }


        parentid = parentid.filter(function(x, i, a) {
            return a.indexOf(x) == i;
        })
        //console.log(parentid)
        //console.log(final_map)

    }
    final_sequnce = {}
    final_sequnce_type = []
    cont = 0
    for (i = 0; i < parentid.length; i++) {

        console.log('--------------')
        console.log(final_map[parentid[i]])
        console.log(typeofCompo[parentid[i]])
        final_sequnce_type.push(typeofCompo[parentid[i]])

        if (typeofCompo[parentid[i]] == 'python') {
            final_sequnce[cont] = final_map[parentid[i]][0]
            cont = cont + 1
        } else if (typeofCompo[parentid[i]] == 'talend') {
            final_sequnce[cont] = final_map[parentid[i]][0]
            cont = cont + 1

        } else if (typeofCompo[parentid[i]] == 'matillion') {
            o = {
                "server": final_map[parentid[i]][0][0],
                "GroupName": final_map[parentid[i]][0][1],
                "ProjectName": final_map[parentid[i]][0][2],
                "Version": final_map[parentid[i]][0][3],
                "JobName": final_map[parentid[i]][0][4],
                "Environment": final_map[parentid[i]][0][5]
            }
            final_sequnce[cont] = o
            cont = cont + 1
        }

    }
    console.log('-----$$$$$$---------')
    console.log(final_sequnce)
    console.log(final_sequnce_type)
    for (i = 0; i < final_sequnce_type.length; i++) {
        if (final_sequnce_type[i] == 'python') {
            console.log('python file ' + final_sequnce[i])
        } else if (final_sequnce_type[i] == 'talend') {
            console.log('talend file ' + final_sequnce[i])
        } else if (final_sequnce_type[i] == 'matillion') {
            console.log('matillion file ' + final_sequnce[i]['server'])

        }

    }

    return [final_sequnce_type, final_sequnce]

}