//import { ReactiveVar } from 'meteor/reactive-var';
import { Template } from 'meteor/templating';
import { Tasks } from '../imports/ui/tasks.js' ;

import './newtodo.html';
import './ubersicht.html';


Template.body.helpers({
	/* das geht:
  todos:[
    {todo: 'todo', deadline: 'deadline', percent: 'percent'},
  ]*/

  //das noch nicht.. greift falsch oder garnicht auf Tasks zu
	todos(){
		return Tasks.find({});
	}
});


