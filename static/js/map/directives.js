mapApp.directive('piece', function () {                                       
    return {                                                                    
        restrict: 'E',                                                          
        scope: {title: '@'},                                                    
        templateUrl: "map_piece.html",                                             
        scope: {                                                                
            'index': '='                                                       
        },                                                                      
        controller: function ($http, $scope, $rootScope) {                      
            $scope.land = LAND[$scope.index] + '-hex';
            $scope.number = NUMBERS[$scope.index];
        }                                                                       
    }                                                                           
});
