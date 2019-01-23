var gulp = require('gulp'),
watch = require('gulp-watch'),
browserSync = require('browser-sync').create();

gulp.task('watch', function() {

  browserSync.init({
    notify: false,
    server: {
      baseDir: "app/src"
    }
  });

  watch('./app/src/templates/*.html', function() {
    browserSync.reload();
  });

  watch('./app/assets/css/**/*.css', function() {
    gulp.start('cssInject');
  });

  watch('./app/assets/js/**/*.js', function() {
    gulp.start('jsInject');
  });

});

gulp.task('cssInject', ['styles'], function() {
  return gulp.src('./app/src/static/css/*.css')
    .pipe(browserSync.stream());
});

gulp.task('jsInject', ['js'], function() {
  return gulp.src('./app/src/static/js/app.jjs')
    .pipe(browserSync.stream());
});


