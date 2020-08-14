const gulp = require("gulp");
const sass = require("gulp-sass");
const sourcemaps = require("gulp-sourcemaps");
const rename = require("gulp-rename");
const del = require("del");
const browserSync = require("browser-sync").create();
const postcss = require("gulp-postcss");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const plumber = require("gulp-plumber");

const paths = {
	styles: {
		src: "./dev/scss/**/*.scss",
		dest: "./static/build/css/",
	},
};

const clean = () => del(["./static/build"]);

// Convert scss to css, auto-prefix and rename into styles.min.css
const styles = () =>
	gulp
		.src(paths.styles.src)
		.pipe(plumber())
		.pipe(sourcemaps.init())
		.pipe(sass().on("error", sass.logError))
		.pipe(postcss([autoprefixer(), cssnano()]))
		.pipe(
			rename({
				basename: "styles",
				suffix: ".min",
			})
		)
		.pipe(sourcemaps.write("."))
		.pipe(gulp.dest(paths.styles.dest))
		.pipe(browserSync.stream());

// Watches all .scss changes and executes the corresponding task
function watchFiles() {
	gulp.watch(paths.styles.src, styles);
}

const build = gulp.series(clean, gulp.parallel(styles));

const watch = gulp.series(build, watchFiles);

exports.clean = clean;
exports.styles = styles;
exports.watch = watch;
exports.build = build;
exports.default = watch;
