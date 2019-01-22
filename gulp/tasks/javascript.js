var gulp = require('gulp');
var concat = require('gulp-concat');


gulp.task('js', function(){
	return gulp.src('./app/assets/js/**/*.js')
				.pipe(concat('app.js'))
				.on('error', function(errorInfo) {
			      console.log(errorInfo.toString());
			      this.emit('end');
			    })
			    .pipe(gulp.dest('./app/src/static/js'));

});