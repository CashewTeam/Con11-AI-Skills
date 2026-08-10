# DefaultStage | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / DefaultStage 
# DefaultStage
```kotlin
fun SpatialAppScope.DefaultStage(content: @Composable StageScope.() -> Unit)
```
The first  Stage  of app, started by PICO OS. Currently must be configured at app's AndroidManifest.xml 
The first  WindowContainer  of app, started by PICO OS. Currently must be configured at app's AndroidManifest.xml 
Your launch activity should be extends  com.pico.spatial.ui.platform.stub.SpatialLaunchActivity 

```
<application>       <activity            android:name=".platform.LaunchActivity"            android:exported="true"            android:theme="@style/Theme.SpatialApp">            <intent-filter>                <action android:name="android.intent.action.MAIN" />                <category android:name="android.intent.category.LAUNCHER" />            </intent-filter>            <meta-data android:name="pico.spatial.stage.id" android:value="MainStage"/>            <meta-data android:name="pico.spatial.stage.style" android:value="0"/>            <meta-data android:name="pico.spatial.stage.immersion" android:value="50"/>            <meta-data android:name="pico.spatial.stage.immersion_min" android:value="0"/>            <meta-data android:name="pico.spatial.stage.immersion_max" android:value="100"/>        </activity></application>
```
need be configured at AndroidManifest, like  DefaultWindowContainer  The app entrance could be one of  DefaultStage  or  DefaultWindowContainer 
#### See also
Stage