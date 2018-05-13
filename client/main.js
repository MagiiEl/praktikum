import { ReactiveVar } from 'meteor/reactive-var';
import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import {Tasks} from '../imports/api/tasks.js' ;

import './newtodo.html';
import './ubersicht.html';

this.ident="";
this.to="";
this.dl="";
this.per="";


Template.body.helpers({
/*
  todos:[
    {ladidadida: "nanananana", todo: 'todo', deadline: 'deadline', percent: 'percent'},
  ]

  //das noch nicht.. greift falsch oder garnicht auf Tasks zu}*/
	todos(){
		return Tasks.find({});
	}
});

Template.newtodo.events({
	'click .btn-success':function(){
		Tasks.insert({
			todo: $('input[id="new-todo"]').val(),
			deadline: $('input[id="new-deadline"]').val(),
			percent: $('input[id="new-percent"]').val()
		});

		$('input[id="new-todo"]').val("");
		$('input[id="new-deadline"]').val("");
		$('input[id="new-percent"]').val("");
	}
});

Template.edittodo.events({
	'click .btn-primary':function(){
		Tasks.update({
			_id: ident,
			//todo: to,
			//deadline: dl,
			//percent: per
		},{
			todo: $('input[id="edit-todo"]').val(),
			deadline: $('input[id="edit-deadline"]').val(),
			percent: $('input[id="edit-percent"]').val()
		});

		$('input[id="edit-todo"]').val("");
		$('input[id="edit-deadline"]').val("");
		$('input[id="edit-percent"]').val("");

		$('#edit-modal').modal('hide')
	}
});

Template.curtodo.events({
	'click .btn-danger': function(){
		Tasks.remove(this._id);
		return false;
	},

	'click .btn-info': function(){
		
		ident = this._id;
		to = this.todo;
		dl = this.deadline;
		per = this.percent;

		$('#edit-modal').modal("show")	
		
	}
});


