# DefaultWindowContainer | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / DefaultWindowContainer 
# DefaultWindowContainer
```kotlin
fun SpatialAppScope.DefaultWindowContainer(content: @Composable WindowContainerScope.() -> Unit)
```
The first  WindowContainer  of app, started by PICO OS. Currently must be configured at app's AndroidManifest.xml 
Your launch activity should be extends  com.pico.spatial.ui.platform.stub.SpatialLaunchActivity 

```
<application>       <activity            android:name=".platform.LaunchActivity"            android:exported="true"            android:theme="@style/Theme.SpatialApp">            <intent-filter>                <action android:name="android.intent.action.MAIN" />                <category android:name="android.intent.category.LAUNCHER" />            </intent-filter>            <meta-data android:name="pico.spatial.windowcontainer.id" android:value="Main"/>            <meta-data android:name="pico.spatial.windowcontainer.defaultsize" android:value="1600x900"/>            <!--specific the resizeType of WindowContainer               0: Default, system default, set to [ContentMinSize] if not changed otherwise               1: ContentMinSize, no smaller than content's minimum size               2: ContentSize, within content's minimum and maximum size            -->            <meta-data android:name="pico.spatial.windowcontainer.resizetype" android:value="0"/>        </activity></application>
```