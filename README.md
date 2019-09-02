<h1>What is it for?</h1>

<p>It can be used to join all meshes inside collection into single mesh (also recursive) in <strong>non-destructive</strong> way.</p>
<p>This might be useful for anyone who wants to optimize their game scenes by merging multiple meshes.</p>

<h1>How to use it?</h1>

<p>Right-click collection in outliner (scene panel). You should see two options, at the end of the context menu:</p>
<ul>
  <li><strong>Join</strong> all meshes assigned to selected collection.</li>
  <li><strong>Join Recursive</strong> all meshes assigned to selected collection <strong>AND</strong> all meshes in descendant collections.</li>
</ul>

<img src="https://lonegamedev.com/wp-content/uploads/2019/09/join-collection.png" />

<p>Resulting object will be appended at the end of collection.</p>

<h1>Installation</h1>

<p>Put this repo directory inside %BLENDER_DIR%/2.80/scripts/addons</p>

<strong>OR</strong>

Use install feature (Edit/Preferences/Add-ons/Install) from inside of Blender

<strong>AND</strong>

don't forget to enable the addon (via preferences mentioned above) ;-)

<h1>Credits:</h1>
<p>bmesh combine function taken from from https://github.com/nortikin/sverchok (GPL3 license)<p>
<h2>Cheers!</h2>
