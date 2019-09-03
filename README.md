<h1>What is it for?</h1>

<p>Probably useful for anyone who wants to optimize their game scenes by merging multiple meshes.</p>

<p>It allows you to join all meshes inside collection into new object. It should help with the workflow when creating complex scenes from mesh tiles.</p>

<img src="https://lonegamedev.com/wp-content/uploads/2019/09/join-collection.png" />

<h1>How to use it?</h1>

<p>Right-click collection in outliner (scene panel). You should see two options, at the end of the context menu:</p>
<ul>
  <li><strong>Join</strong> all meshes assigned to selected collection.</li>
  <li><strong>Join Recursive</strong> all meshes assigned to selected collection <strong>AND</strong> all meshes in descendant collections.</li>
</ul>

<p>Resulting object will be appended at the end of collection.</p>

<h1>Installation</h1>

<p>Put inside %BLENDER_DIR%/2.80/scripts/addons</p>

<strong>OR</strong>

<p>Use install feature (Edit/Preferences/Add-ons/Install) from inside of Blender</p>

<strong>AND</strong>

<p>don't forget to enable the addon (via preferences mentioned above) ;-)</p>

<h1>Requires</h1>
<p>Blender 2.80 obviously, since this is the version that introduced collections.</p>

<h1>Credits</h1>
<p>bmesh combine function taken from from https://github.com/nortikin/sverchok (GPL3 license)<p>
  
<h2>Cheers!</h2>
