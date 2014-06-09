var myapp = angular.module('myapp',[]);
myapp.factory('Data',function(){
	return {message:"i got it"} 
})

function first($scope,Data){
	$scope.data = Data;

	$scope.revert = function(message){
		return message.split("").reverse().join("");
	}
}

function firstone ($scope,Data) {
	// body...
	$scope.data = Data;
}