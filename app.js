/*
Code reference
https://medium.com/@necsoft/three-js-101-hello-world-part-1-443207b1ebe1
*/

var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
camera.position.z = 4;

var renderer = new THREE.WebGLRenderer({antialias:true});

renderer.setClearColor("#000000");

renderer.setSize( window.innerWidth, window.innerHeight );
renderer.shadowMap.enabled = true;

document.body.appendChild( renderer.domElement );
   
const geometry = new THREE.SphereGeometry(1, 32, 32); 
const material = new THREE.MeshStandardMaterial({ color: 0x0077ff }); 
const sphere = new THREE.Mesh(geometry, material);
sphere.castShadow = true; 
scene.add(sphere); 

const planeGeometry = new THREE.PlaneGeometry(10, 10);
const planeMaterial = new THREE.ShadowMaterial({ opacity: 0.5 });  
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = - Math.PI / 2;  
plane.position.y = -2; 
plane.receiveShadow = true;  
scene.add(plane);  


const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 5);  
light.castShadow = true;  
scene.add(light);  


light.shadow.mapSize.width = 512;  
light.shadow.mapSize.height = 512; 
light.shadow.camera.near = 0.5; 
light.shadow.camera.far = 10; 

var render = function () {
  requestAnimationFrame( render );

  sphere.rotation.x += 0.01;
  sphere.rotation.y += 0.01;


  renderer.render(scene, camera);
};

render();